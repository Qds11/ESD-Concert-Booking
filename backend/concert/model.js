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
    if (rows.length === 0) {
      return { status: 400, data: "There are no concerts with this id" };
    }
    return { status: 200, data: rows };
  } catch (err) {
    return { status: 500, data: err.message };
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
export async function updateConcertStatus(id, status) {
  try {
    await db.query(
      `UPDATE concert SET status = ? WHERE concert_id = ?`,
      [status, id]
    );
    return { code: 200, message: "status updated" };
  } catch (err) {
    return { code: 500, message: "failed to update status" };
  }
}

