import express from "express";
import {
  RECOMMENDATION_MICROSERVICE_URL,
  TICKETING_MICROSERVICE_URL,
} from "./config.js";
//import function from models.js
import {
  getConcertById,
  getAllConcertData,
  updateConcertStatus,
} from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";
import axios from 'axios';


const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//get all concerts
app.get("/", async (req, res) => {
  const concerts = await getAllConcertData();
  const userId = req.query.userid;
   console.log(userId)
  if (userId) {
    const recommended = await axios.get(
      `${RECOMMENDATION_MICROSERVICE_URL}/${userId}`
    );
    return res.json({ concerts: concerts, recommended: recommended.data });
  }
  return res.json({concerts:concerts,recommended:null})
 });


 //get concert by id and checks status
app.get("/concert/:id", async (req, res) => {
  const id = req.params.id;
  const result = await getConcertById(id);
  const concert = result.data;
  if (concert[0].status && concert[0].status === "closed") {
    res.json(concert);
    return;
  }
  if (concert[0].status && concert[0].status.includes("available")) {
    try {
      const {
        data: { status },
      } = await axios.get(`${TICKETING_MICROSERVICE_URL}/${id.toString()}`);
      if (status.includes("sold out")) {
        await updateConcertStatus(id, status);
        concert[0].status = status;
      }
    } catch (err) {
      console.log(err);
    }
  }
  res.json(concert);
});

//get concert by genre (for recommendation)
app.get("/concert/:genre", async (req, res) => {
  const genre = req.params.genre;
  const concert = await getConcertByGenre(genre);
  res.json(concert);
});


// app.get("/reco/:id", async (req, res) => {
//   try {
//     const userId = req.params.id;
//    // console.log(userId)
//     //const userId=1
//     const url = `${RECOMMENDATION_MICROSERVICE_URL}/${userId}`;
//     const response = await axios.get(url);
//     const genre = response.data.message
//     const concert = await getConcertByGenre(genre);

//     // Send the response back to the frontend
//     console.log(concert)
//     res.send(concert)
//     console.log(response.data);
//     // res.send(response.data);
//   } catch (error) {
//     console.error(error);
//     res.sendStatus(500);
//   }
// });

//PORT
app.listen(5005, () => {
  console.log("Server is running on port 5005");
});
