#!/usr/bin/node

const request = require('request');
const requestUrl = process.argv[2];

request(requestUrl, (err, response, body) => {
  if (err) {
    throw (err);
  }
  const tasks = {};
  const todos = JSON.parse(body);
  let completed = 0;
  let prevId = 0;
  for (const todo of todos) {
    if (todo.completed && prevId === todo.userId) {
      completed += 1;
      tasks[todo.userId] = completed;
    } else if (todo.completed && prevId === 0) {
      tasks[todo.userId] = completed++;
    } else if (todo.completed && prevId !== todo.userId) {
      completed = 0;
      completed += 1;
      tasks[todo.userId] = completed;
    } else if (prevId !== todo.userId && !todo.completed) {
      completed = 0;
    }
    prevId = todo.userId;
  }
  console.log(tasks);
});
