import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array passing Number', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('display a error message if jobs is not an array passing Object', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('display a error message if jobs is not an array passing String', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
    // expect(queue.testMode.job[0]);
  });

  it('should NOT display a error message if jobs is an array with empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
    // expect(queue.testMode.job[0]);
  });

  it('create two new jobs to the queue', () => {
    queue.createJob('myJob', { foo: 'bar' }).save();
    queue.createJob('anotherJob', { baz: 'bip' }).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('myJob');
    expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
    expect(queue.testMode.jobs[1].type).to.equal('anotherJob');
    expect(queue.testMode.jobs[1].data).to.eql({ baz: 'bip' });
  });
});
