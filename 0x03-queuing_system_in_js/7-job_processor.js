import kue from "kue";

// Create a queue
const queue = kue.createQueue();

// Array containing blacklisted phone numbers
const blacklisted = ["4153518780", "4153518781"];

// Function to send notification
const sendNotification = (phoneNumber, message, job, done) => {
	job.progress(0, 100); // Track progress to 0%
	if (blacklisted.includes(phoneNumber)) {
		done(new Error(`Phone number ${phoneNumber} is blacklisted`));
	} else {
		job.progress(50, 100); // Track progress to 50%
		console.log(
			`Sending notification to ${phoneNumber}, with message: ${message}`
		);
		return done(); // Mark job as done
	}
};

// Process the queue with 2 concurrent jobs
queue.process("push_notification_code_2", 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
