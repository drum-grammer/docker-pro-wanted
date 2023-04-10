from flask import Flask, render_template, request, jsonify, make_response, Response
import requests
import logging

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("http://hls_to_rtmp:5001/get_twitch_url")
    response.raise_for_status()
    twitch_url = response.json().get("twitch_url", "")
    return render_template("index.html", twitch_url=twitch_url)


@app.route("/update", methods=["POST"])
def update():
    try:
        data = request.get_json()
        twitch_url = data.get("twitch_url")
        response = requests.post("http://hls_to_rtmp:5001/update", json={"twitch_url": twitch_url})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.exception("Error in update()")
        return jsonify({"error": str(e)}), 500


@app.route("/hls/<path:path>")
def hls_proxy(path):
    try:
        hls_url = f"http://mock_rtmp_server/hls/{path}"
        response = requests.get(hls_url)
        response.raise_for_status()
        if path.endswith(".m3u8"):
            content_type = "application/vnd.apple.mpegurl"
        else:
            content_type = "video/MP2T"
        content = response.content
        return Response(content, content_type=content_type)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/resource_usage")
def resource_usage():
    try:
        response = requests.get("http://hls_to_rtmp:5001/resource_usage")
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/resource_usage_csv")
def resource_usage_csv():
    response = requests.get("http://hls_to_rtmp:5001/resource_usage.csv")
    response_data = make_response(response.content)
    response_data.headers["Content-Disposition"] = "attachment; filename=resource_usage.csv"
    response_data.headers["Content-Type"] = "text/csv"
    return response_data


@app.route("/resource_usage_json")
def resource_usage_json():
    response = requests.get("http://hls_to_rtmp:5001/resource_usage.json")
    response_data = make_response(response.content)
    response_data.headers["Content-Disposition"] = "attachment; filename=resource_usage.json"
    response_data.headers["Content-Type"] = "application/json"
    return response_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
