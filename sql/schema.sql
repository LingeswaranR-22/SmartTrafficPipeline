CREATE TABLE IF NOT EXISTS traffic_incidents (
    id SERIAL PRIMARY KEY,
    incident_time TIMESTAMP,
    location VARCHAR(200),
    latitude FLOAT,
    longitude FLOAT,
    incident_type VARCHAR(100),
    severity VARCHAR(50)
);

