import redis from "redis";

const client = redis.createClient();
client.flushdb();

client.on("connect", () => {
	console.log("Redis client connected to the server");
});


client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

const channelName = "holberton school channel";
client.subscribe(channelName);

client.on("message", (_, message) => {
	if (message === "KILL_SERVER") {
		client.unsubscribe(channelName);
		client.quit();
	}
	console.log(`${message}`);
});
