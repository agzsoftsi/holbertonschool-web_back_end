import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending ',
  };
  const promise2 = {
    status: 'pending ',
  };

  try {
    const signup = await signUpUser(firstName, lastName);
    promise1.status = 'fulfilled';
    promise1.value = signup;
  } catch (err) {
    promise1.status = 'rejected';
    promise1.value = err.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    promise2.status = 'fulfilled';
    promise2.value = upload;
  } catch (err) {
    promise2.status = 'rejected';
    promise2.value = err.toString();
  }

  return [promise1, promise2];
}

export default handleProfileSignup;
