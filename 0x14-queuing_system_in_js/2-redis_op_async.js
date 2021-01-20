import redis from 'redis';
// Task 2 - asycn Implemnetation
import { promisify } from 'util';

const cli = redis.createClient();
const addAsync = promisify(cli.get).bind(cli);

cli.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cli.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Task 1
function setNewSchool(schoolName, value) {
  cli.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  cli.get(schoolName, (err, res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
