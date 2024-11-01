CREATE TYPE active_status AS ENUM ('ACTIVE', 'INACTIVE');
CREATE TYPE level AS ENUM('BEGINNER', 'INTERMEDIATE', 'EXPERT');
CREATE TYPE gender AS ENUM('MALE', 'FEMALE', 'OTHER');

CREATE TABLE IF NOT EXISTS "coach"
(
    "id" UUID NOT NULL,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "email" VARCHAR(50) NOT NULL,
    "password" VARCHAR(50) NOT NULL,
    "user_name" VARCHAR(50) NOT NULL,
    "status" active_status NOT NULL,
    "created_by" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP,
    "modified_by" VARCHAR(100),
    "modified_at" TIMESTAMP,
    CONSTRAINT "coach_pkey" PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "athlete"
(
    "id" UUID NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "event" VARCHAR(200) NOT NULL,
    "contact" INT NOT NULL,
    "dob" DATE NOT NULL,
    "level" level,
    "heart_rate" VARCHAR(200) NOT NULL,
    "gender" gender,
    "weight" DECIMAL(10, 2),
    "height" DECIMAL(10, 2),
    "personal_best" VARCHAR(200) NOT NULL,
    "status" active_status,
    "coach_id" UUID,
    "created_by" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP,
    "modified_by" VARCHAR(100),
    "modified_at" TIMESTAMP,
     CONSTRAINT fk_coach FOREIGN KEY ("coach_id") REFERENCES "coach"("id")
);

CREATE TABLE IF NOT EXISTS "session"
(
    "id" UUID NOT NULL PRIMARY KEY ,
    "name" VARCHAR(200) NOT NULL,
    "session_date" DATE NOT NULL,
    "venue_date" DATE NOT NULL,
    "start_time" TIMESTAMP,
    "end_date" TIMESTAMP,
    "is_completed" BOOLEAN,
    "status" active_status,
    "created_by" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP,
    "modified_by" VARCHAR(100),
    "modified_at" TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "session_detail"
(
    "id" UUID NOT NULL PRIMARY KEY,
    "session_id" UUID NOT NULL,
    "athlete_id" UUID NOT NULL,
    "race_time" VARCHAR(100) NOT NULL,
    "heart_rate_detail" TEXT,
    "distance" DECIMAL(10, 2),
    "distance_type" VARCHAR(20) NOT NULL,
    "status" active_status,
        "created_by" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP,
    "modified_by" VARCHAR(100),
    "modified_at" TIMESTAMP,
    CONSTRAINT fk_session_id FOREIGN KEY ("session_id") REFERENCES "session"("id"),
    CONSTRAINT fk_athlete_id FOREIGN KEY ("athlete_id") REFERENCES "athlete"("id")
)