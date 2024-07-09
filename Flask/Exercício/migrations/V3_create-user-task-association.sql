CREATE TABLE user_task_association (
    user_id VARCHAR(100) REFERENCES users(user_id),
    task_id VARCHAR(100) REFERENCES tasks(task_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, task_id)
);
