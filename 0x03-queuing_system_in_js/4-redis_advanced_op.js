import redis from "redis";

const client = redis.createClient();
client.flushdb();

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

const cityCounts = {
	Portland: "50",
	Seattle: "80",
	"New York": "20",
	Bogota: "20",
	Cali: "40",
	Paris: "2",
};

const hashName = "HolbertonSchools";
Object.entries(cityCounts).forEach(([city, count]) => {
	client.hset(hashName, city, count, redis.print);
});

client.hgetall(hashName, (err, gotAll) => {
	if (err) {
		console.log(`Error retrieving data: ${err}`);
	} else {
		console.log(gotAll);
	}
});