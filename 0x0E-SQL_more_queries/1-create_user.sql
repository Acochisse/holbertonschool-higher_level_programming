-- Script that creates a new user with all permissions on server

CREATE USER IF NOT EXISTS "user_0d_1""@""localhost";
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
