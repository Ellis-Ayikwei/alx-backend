import express from "express";
import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();
const port = 1245;
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

const listProducts = [
	{ id: 1, name: "Suitcase 250", price: 50, stock: 4 },
	{ id: 2, name: "Suitcase 450", price: 100, stock: 10 },
	{ id: 3, name: "Suitcase 650", price: 350, stock: 2 },
	{ id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

const getItemById = (id) => {
	return listProducts.find((product) => product.id === id);
};

const getItemStock = (id) => {
	const item = listProducts.find((product) => product.id === id);
	return item ? item.stock >= 1 : false;
};

const reserveStockById = (item, stock) => {
	client.set(item.id, stock);
};

const getCurrentReservedStockById = async (itemId) => {
	const rsvstock = await getAsync(itemId);
	return rsvstock === 0 ? { status: "Product not found" } : rsvstock;
	// return new Promise((resolve, reject) => {
	// 	client.get(itemId, (err, data) => {
	// 		if (err) {
	// 			reject(err);
	// 		} else if (data <= 0) {
	// 			resolve({ status: "Product not found" });
	// 		} else {
	// 			resolve(data);
	// 		}
	// 	});
	// });
};

const app = express();

app.get("/list_products", (req, res) => {
	res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
	const item_id = req.params.itemId;
	const stock = await getCurrentReservedStockById(parseInt(item_id));
	res.json(stock);
});

app.get("/reserve_product/:itemId", (req, res) => {
	const item_id = parseInt(req.params.itemId);
	const item = getItemById(item_id);
	console.log(item);
	if (!item) {
		res.json({ status: "Product not found" });
	}
	const item_gotten = getItemStock(item_id);
	if (!item_gotten) {
		res.json({ status: "Not enough stock available", itemId: item_id });
	}
	reserveStockById;
	res.json({ status: "Reservation confirmed", itemId: 1 });
});

app.listen(port, () => {
	console.log(`The express server is listening on the port ${port}`);
});
