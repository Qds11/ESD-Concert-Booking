import db from "./db.js";
// import moment from "moment";


export async function getAllConcertData() {
  const [rows] = await db.query("select * from concert");
  const concerts = [];
  return rows;
}

export async function getConcertById(id) {
    try {
        const [rows] = await db.query(
          `select * from concert where concert_id = ?`,
          [id]
        );
        return rows
    } catch (err) {
        return (err)
      }
}
