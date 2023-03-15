import mysql from "mysql2";

//create connection to database
const db = mysql
  .createPool({
    host: "localhost",
    user: "root",
    password: "",
    database: "concertdata",
  })
  .promise();

export default db;
