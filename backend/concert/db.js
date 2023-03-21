import mysql from "mysql2";

//create connection to database
const db = mysql
  .createPool({
    host: "localhost",
    user: "root",
    password: "root",
    database: "concertdata",
    // host: "sql12.freesqldatabase.com",
    // user: "sql12606226",
    // password: "61vMwF9lhJ",
    // database: "sql12606226",
    port:8889,
  })
  .promise();

export default db;
