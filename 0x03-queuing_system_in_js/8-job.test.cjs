// test/notifications.test.js
import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";
describe("createPushNotificationsJobs", () => {
	let queue;

	before(() => {
		queue = kue.createQueue();
		queue.testMode.enter();
	});

	after(() => {
		queue.testMode.exit();
	});

	afterEach(() => {
		queue.clear();
	});

	it("should create jobs in the queue", () => {
		const jobs = [
			{ phoneNumber: "4153518780", message: "Test message 1" },
			{ phoneNumber: "4153518781", message: "Test message 2" },
		];

		createPushNotificationsJobs(jobs);

		const queuedJobs = queue.testMode.jobs;

		expect(queuedJobs.length).to.equal(2);
		expect(queuedJobs[0].data.phoneNumber).to.equal("4153518780");
		expect(queuedJobs[1].data.phoneNumber).to.equal("4153518781");
	});

	it("should handle an empty jobs array", () => {
		createPushNotificationsJobs([]);

		const queuedJobs = queue.testMode.jobs;

		expect(queuedJobs.length).to.equal(0);
	});
});
