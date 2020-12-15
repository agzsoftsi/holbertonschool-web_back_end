![](Top.png)


# Requirements

## General

> - All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
> - Allowed editors: vi, vim, emacs, Visual Studio Code
> - All your files should end with a new line
> - A README.md file, at the root of the folder of the project, is mandatory
> - Your code should use the js extension
> - Your code will be tested using Jest and the command npm run test
> - Your code will be analyzed using the linter ESLint along with specific rules that we’ll provide
> - All of your functions must be exported

## Setup

### Install NodeJS 12.11.x

(in your home directory):

```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

```sh
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

## Install Jest, Babel, and ESLint

in your project directory:

- Install Jest using: npm install --save-dev jest
- Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
- Install ESLint using: npm install --save-dev eslint

## Configuration files

### package.json

```sh

{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}

```

### babel.config.js

### utils.js

Use when you get to tasks requiring uploadPhoto and createUser.

```sh
export function uploadPhoto() {
  return Promise.resolve({
    status: 200,
    body: 'photo-profile-1',
  });
}


export function createUser() {
  return Promise.resolve({
    firstName: 'Guillaume',
    lastName: 'Salva',
  });
}

```

```sh
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```
### .eslintrc.js

```sh
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};

```

### Finally…

Don’t forget to run $ npm install when you have the package.json

### Response Data Format

uploadPhoto returns a response with the format

```sh
{
  status: 200,
  body: 'photo-profile-1',
}
```

createUser returns a response with the format

```sh
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```

## Task

**0. Keep every promise you make and only make promises you can keep**
File: [0-promise.js](0-promise.js/) - [0-main.js](0-main.js/)

Return a Promise using this prototype function getResponseFromAPI()

```sh
bob@dylan:~$ cat 0-main.js
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
true
bob@dylan:~$ 
```

**1. Don't make a promise...if you know you can't keep it**
File: [1-promise.js](1-promise.js/) - [1-main.js](1-main.js/)

Using the prototype below, return a promise. The parameter is a boolean.

```sh
getFullResponseFromAPI(success)
```
When the argument is:

- true
> - resolve the promise by passing an object with 2 attributes:
> > - status: 200
> > - body: 'Success'
- false
> - reject the promise with an error object with the message The fake API is not working currently

Try testing it out for yourself

```sh
bob@dylan:~$ cat 1-main.js
import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 1-main.js 
Promise { { status: 200, body: 'Success' } }
Promise {
  <rejected> Error: The fake API is not working currently
    ...
    ...
bob@dylan:~$ 
```

**2. Catch me if you can! **
File: [2-then.js](2-then.js/) - [2-main.js](2-main.js/)

Using the function prototype below

```sh
function handleResponseFromAPI(promise)
```
Append three handlers to the function:

- When the Promise resolves, return an object with the following attributes
> - status: 200
> - body: success
- When the Promise rejects, return an empty Error object
- For every resolution, log Got a response from the API to the console

```sh
bob@dylan:~$ cat 2-main.js
import handleResponseFromAPI from "./2-then";

const promise = Promise.resolve();
handleResponseFromAPI(promise);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 2-main.js 
Got a response from the API
bob@dylan:~$ 
```

**3. Handle multiple successful promises**
File: [3-all.js](3-all.js/) - [3-main.js](3-main.js/)

In this file, import uploadPhoto and createUser from utils.js

Knowing that the functions in utils.js return promises, use the prototype below to collectively resolve all promises and log body firstName lastName to the console.

```sh
function handleProfileSignup()
```

In the event of an error, log Signup system offline to the console

```sh
bob@dylan:~$ cat 3-main.js
import handleProfileSignup from "./3-all";

handleProfileSignup();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 3-main.js 
photo-profile-1 Guillaume Salva
bob@dylan:~$ 
```

**4. Simple promise**
File: [4-user-promise.js](4-user-promise.js/) - [4-main.js](4-main.js/)

Using the following prototype

```sh
function signUpUser(firstName, lastName) {
}
```
That returns a resolved promise with this object:

```sh
{
  firstName: value,
  lastName: value,
}
```

```sh
bob@dylan:~$ cat 4-main.js
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan"));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 4-main.js 
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
bob@dylan:~$ 
```

**5. Reject the promises**
File: [5-photo-reject.js](5-photo-reject.js/) - [5-main.js](5-main.js/)

Write and export a function named uploadPhoto. It should accept one argument fileName (string).

The function should return a Promise rejecting with an Error and the string $fileName cannot be processed

```sh
export default function uploadPhoto(filename) {

}
```

```sh
bob@dylan:~$ cat 5-main.js
import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg'));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 5-main.js 
Promise {
  <rejected> Error: guillaume.jpg cannot be processed
  ..
    ..
bob@dylan:~$ 
```

**6. Handle multiple promises**
File: [6-final-user.js](6-final-user.js/) - [6-main.js](6-main.js/)

Import signUpUser from 4-user-promise.js and uploadPhoto from 5-photo-reject.js.

Write and export a function named handleProfileSignup. It should accept three arguments firstName (string), lastName (string), and fileName (string). The function should call the two other functions. When the promises are all settled it should return an array with the following structure:

```sh
[
    {
      status: status_of_the_promise,
      value: value or error returned by the Promise
    },
    ...
  ]
```

```sh
bob@dylan:~$ cat 6-main.js
import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 6-main.js 
Promise { <pending> }
bob@dylan:~$ 
```

**7. Load balancer**
File: [7-load_balancer.js](7-load_balancer.js/) - [7-main.js](7-main.js/)

Write and export a function named loadBalancer. It should accept two arguments chinaDownload (Promise) and USDownload (Promise).

The function should return the value returned by the promise that resolved the first.

```sh
export default function loadBalancer(chinaDownload, USDownload) {

}
```

```sh
bob@dylan:~$ cat 7-main.js
import loadBalancer from "./7-load_balancer";

const ukSuccess = 'Downloading from UK is faster';
const frSuccess = 'Downloading from FR is faster';

const promiseUK = new Promise(function(resolve, reject) {
    setTimeout(resolve, 100, ukSuccess);
});

const promiseUKSlow = new Promise(function(resolve, reject) {
    setTimeout(resolve, 400, ukSuccess);
});

const promiseFR = new Promise(function(resolve, reject) {
    setTimeout(resolve, 200, frSuccess);
});

const test = async () => {
    console.log(await loadBalancer(promiseUK, promiseFR));
    console.log(await loadBalancer(promiseUKSlow, promiseFR));
}

test();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 7-main.js 
Downloading from UK is faster
Downloading from FR is faster
bob@dylan:~$ 
```

**8. Throw error / try catch**
File: [8-try.js](8-try.js/) - [8-main.js](8-main.js/)

Write a function named divideFunction that will accept two arguments: numerator (Number) and denominator (Number).

When the denominator argument is equal to 0, the function should throw a new error with the message cannot divide by 0. Otherwise it should return the numerator divided by the denominator.

```sh
export default function divideFunction(numerator, denominator) {

}
```

```sh
bob@dylan:~$ cat 8-main.js
import divideFunction from './8-try';

console.log(divideFunction(10, 2));
console.log(divideFunction(10, 0));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 8-main.js 
5
..../8-try.js:15
  throw Error('cannot divide by 0');
  ^
.....

bob@dylan:~$ 
```

**9. Throw an error**
File: [9-try.js](9-try.js/) - [9-main.js](9-main.js/)

Write a function named guardrail that will accept one argument mathFunction (Function).

This function should create and return an array named queue.

When the mathFunction function is executed, the value returned by the function should be appended to the queue. If this function throws an error, the error message should be appended to the queue. In every case, the message Guardrail was processed should be added to the queue.

Example:

```sh
[
  1000,
  'Guardrail was processed',
]
```

```sh
bob@dylan:~$ cat 9-main.js
import guardrail from './9-try';
import divideFunction from './8-try';

console.log(guardrail(() => { return divideFunction(10, 2)}));
console.log(guardrail(() => { return divideFunction(10, 0)}));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js 
[ 5, 'Guardrail was processed' ]
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
bob@dylan:~$ 
```

**10. Await / Async**
File: [100-await.js](100-await.js/) - [100-main.js](100-main.js/)

Import uploadPhoto and createUser from utils.js

Write an async function named asyncUploadUser that will call these two functions and return an object with the following format:

```sh
{
  photo: response_from_uploadPhoto_function,
  user: response_from_createUser_function,
}
```
If one of the async function fails, return an empty object. Example:

```sh
{
  photo: null,
  user: null,
}
```

```sh
bob@dylan:~$ cat 100-main.js
import asyncUploadUser from "./100-await";

const test = async () => {
    const value = await asyncUploadUser();
    console.log(value);
};

test();

bob@dylan:~$ 
bob@dylan:~$ npm run dev 100-main.js 
{
  photo: { status: 200, body: 'photo-profile-1' },
  user: { firstName: 'Guillaume', lastName: 'Salva' }
}
bob@dylan:~$ 
```