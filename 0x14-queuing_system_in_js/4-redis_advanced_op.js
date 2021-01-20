import redis from 'redis';

const cli = redis.createClient();

cli.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cli.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Task 4

const KEYHASH = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  cli.hset(KEYHASH, key, values[index], redis.print);
});

cli.hgetall(KEYHASH, (err, value) => {
  console.log(value);
});
