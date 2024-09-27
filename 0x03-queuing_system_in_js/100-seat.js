import redis from "redis";
const client = redis.createClient()
import kue from 'kue'
import express from "express";
import { promisify } from "util";

const app = express()
const port =  1245

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

const queue = kue.createQueue();

const asyncGet = promisify(client.get).bind(client);
const asyncSet = promisify(client.set).bind(client)
const reservationEnabled = true;

const number = 50;

const reserveSeat = async (number) => {
	await asyncSet("available_seats", number);
};

const getCurrentAvailableSeats = async () => {
	return await asyncGet("available_seats");
};

app.get('/available_seats', async (req, res) => {
	const availableSeats = await getCurrentAvailableSeats();
    console.log("availbale sets", availableSeats)
	res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', async (req, res) => {
	if (!reservationEnabled) {
		return res.json({ status: "Reservation are blocked" });
	}

	const job = queue.create('reserve_seat').save((err) => {
		if (!err) {
			res.json({ status: "Reservation in process" });
		} else {
			res.json({ status: "Reservation failed" });
		}
	});

	job
		.on('complete', () => {
			console.log(`Seat reservation job ${job.id} completed`);
		})
		.on('failed', (errorMessage) => {
			console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
		});
});

app.get('/process', async (req, res) => {
	res.json({ status: "Queue processing" });

	await queue.process('reserve_seat', async (job, done) => {
		const availableSeats = await getCurrentAvailableSeats();
		const newAvailableSeats = parseInt(availableSeats) - 1;

		if (newAvailableSeats < 0) {
			return done(new Error('Not enough seats available'));
		}

		await reserveSeat(newAvailableSeats);

		if (newAvailableSeats === 0) {
			reservationEnabled = false;
		}

		done();
	});
});

app.listen(port, () => {
	console.log(`the app has started listening on port ${port}`);
});

(async () => {
	await reserveSeat(number);
})();
