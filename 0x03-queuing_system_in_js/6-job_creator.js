import kue from "kue";
const queue = kue.createQueue();

const jobData = {
	phoneNumber: "4155551234",
	message: "This is a system notification message from Holberton School",
};

const job = queue.create("push_notification_code", jobData).save((err) => {
	if (!err) console.log(`Notification job created: ${job.id}`);
});

job
	.on("complete", () => {
		console.log("Notification job completed");
	})
	.on("failed attempt", (errorMessage, doneAttempts) => {
		console.log(`Notification job failed`);
	});

queue.process("push_notification_code", (job, done) => {
	done();
});

