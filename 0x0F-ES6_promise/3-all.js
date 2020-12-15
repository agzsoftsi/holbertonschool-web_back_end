import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const { body } = values[0];
      const { firstName } = values[1];
      const { lastName } = values[1];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup;
