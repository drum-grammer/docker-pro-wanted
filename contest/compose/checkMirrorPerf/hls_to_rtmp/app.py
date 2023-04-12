import subprocess
import threading
import time
import signal
import psutil
from flask import Flask, request, jsonify, make_response
from datetime import datetime
import logging

app = Flask(__name__)

streamlink_resource_usage = {"cpu": 0, "ram": 0}
ffmpeg_resource_usage = {"cpu": 0, "ram": 0}
resource_usage_history = []
max_history_length = 1000
ffmpeg_monitor = None
streamlink_monitor = None
ffmpeg_process = None
streamlink_process = None
current_twitch_url = ""
should_stop_streaming = threading.Event()
logging.basicConfig(level=logging.DEBUG)
_ = list(psutil.process_iter())


def stop_process(process):
    if process:
        process.send_signal(signal.SIGTERM)
        process.wait()


def monitor_resource_usage(process, resource_usage_):
    while not should_stop_streaming.is_set():
        try:
            cmd = f"ps -p {process.pid} -o %cpu,rss"
            output = subprocess.check_output(cmd, shell=True, text=True).splitlines()
            cpu_mem = output[1].split()
            resource_usage_["cpu"] = float(cpu_mem[0])
            resource_usage_["ram"] = float(cpu_mem[1]) / 1024  # Convert KB to MB
        except subprocess.CalledProcessError:
            logging.warning(f"Process with PID {process.pid} not found.")
            break
        except Exception as e:
            logging.exception(f"Error in monitor_resource_usage: {str(e)}")
            break
        time.sleep(1)


def stream_hls_to_rtmp(twitch_url):
    global streamlink_process, ffmpeg_process
    streamlink_command = ["streamlink", "-O", twitch_url, "best"]
    ffmpeg_command = [
        "ffmpeg",
        "-i", "-",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-ar", "44100",
        "-ab", "128k",
        "-strict", "-2",
        "-flags", "+global_header",
        "-bsf:a", "aac_adtstoasc",
        "-f", "flv",
        "rtmp://mock_rtmp_server/live/stream",
    ]

    streamlink_process = subprocess.Popen(streamlink_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ffmpeg_process = subprocess.Popen(ffmpeg_command, stdin=streamlink_process.stdout, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

    return streamlink_process, ffmpeg_process


@app.route("/update", methods=["POST"])
def update():
    global streamlink_monitor, ffmpeg_monitor, streamlink_process, ffmpeg_process
    data = request.json
    twitch_url = data.get("twitch_url", "")

    if ffmpeg_monitor:
        should_stop_streaming.set()
        stop_process(streamlink_process)
        stop_process(ffmpeg_process)
        ffmpeg_monitor.join()

    should_stop_streaming.clear()
    streamlink_process, ffmpeg_process = stream_hls_to_rtmp(twitch_url)
    streamlink_monitor = threading.Thread(target=monitor_resource_usage,
                                          args=(streamlink_process, streamlink_resource_usage))
    ffmpeg_monitor = threading.Thread(target=monitor_resource_usage,
                                      args=(ffmpeg_process, ffmpeg_resource_usage))
    ffmpeg_monitor.start()
    streamlink_monitor.start()

    return jsonify({"message": "Updated successfully"})


@app.route("/resource_usage")
def resource_usage():
    current_usage = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "streamlink": streamlink_resource_usage,
        "ffmpeg": ffmpeg_resource_usage,
    }
    resource_usage_history.append(current_usage)
    if len(resource_usage_history) > max_history_length:
        resource_usage_history.pop(0)
    return jsonify(current_usage)


@app.route("/get_twitch_url")
def get_twitch_url():
    return jsonify({"twitch_url": current_twitch_url})


@app.route("/resource_usage.csv")
def resource_usage_csv():
    csv_data = "timestamp,cpu_total,ram_total,cpu_streamlink,ram_streamlink,cpu_ffmpeg,ram_ffmpeg\n"
    for record in resource_usage_history:
        csv_data += f'{record["timestamp"]},{record["streamlink"]["cpu"] + record["ffmpeg"]["cpu"]},{record["streamlink"]["ram"] + record["ffmpeg"]["ram"]},{record["streamlink"]["cpu"]},{record["streamlink"]["ram"]},{record["ffmpeg"]["cpu"]},{record["ffmpeg"]["ram"]}\n'

    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=resource_usage.csv"
    response.headers["Content-Type"] = "text/csv"
    return response


@app.route("/resource_usage.json")
def resource_usage_json():
    response_data = make_response(jsonify(resource_usage_history))
    response_data.headers["Content-Disposition"] = "attachment; filename=resource_usage.json"
    response_data.headers["Content-Type"] = "application/json"
    return response_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
