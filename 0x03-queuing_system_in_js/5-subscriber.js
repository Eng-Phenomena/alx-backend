import { createClient } from 'redis';

const redisClient = createClient();

//connect to redis server
redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

