import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

// Promisify Redis methods to use async/await
const getAsync = promisify(client.get).bind(client);

// Set up event listeners
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print); // Log response using redis.print
};

const displaySchoolValue = async (schoolName) => {
	const value = await getAsync(schoolName);
	console.log(value);
};

// Define an async function to manage execution flow
(async () => {
	await displaySchoolValue("Holberton"); // Try to get the value first
	setNewSchool("HolbertonSanFrancisco", "100"); // Set a new value
	await displaySchoolValue("HolbertonSanFrancisco"); // Get the new value
})();
