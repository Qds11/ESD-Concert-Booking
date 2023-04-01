import db from "./db.js";
// import moment from "moment";
// const db = process.env.dbURL || 'default value';

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
export async function getConcertByGenre(genre) {
    try {
        const [rows] = await db.query(`select * from concert where genre = ?`, [
          genre,
        ]);
        return rows
    } catch (err) {
        return (err)
      }
}
