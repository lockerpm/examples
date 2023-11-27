import { Locker } from 'lockerpm'

const locker = new Locker({
  accessKeyId: '<your access key id>',
  accessKeySecret: '<your access key secret>',
  apiBase: '<your api base, default is https://secrets-core.locker.io>',
})

async function saveWallet(address: string, privateKey: string) {
  await locker.create({
    key: address,
    value: privateKey,
  })
}

async function getWallet(address: string) {
  const secret = await locker.get(address)
  return {
    address,
    privateKey: secret.value,
  }
}
