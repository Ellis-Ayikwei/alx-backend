import kue from "kue";
const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(
        `Sending notification to ${phoneNumber} with message: ${message}`
    );
};

// Process the jobs in the queue
queue.process("push_notification_code", (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    
    // Mark the job as done
    done();
});

