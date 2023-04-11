const express = require("express");
const app = express();
const port = 8000;

const toDoLists = ["first task"];

app.set("view engine", "pug");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index", {
    toDolistTitle: "To Do Today : " + toDoLists.length,
    toDoLists: toDoLists,
  });
});

app.post("/add-list", (req, res) => {
  const newContent = req.body.content;
  console.log("Add " + newContent);
  toDoLists.push(newContent);
  res.redirect("/");
});

app.listen(port, () => {
  console.log("connected!");
});
