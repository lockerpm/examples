// yarn add lockerpm

import { Locker } from 'lockerpm'

const locker = new Locker({
  accessKeyId: 'xxxx',
  accessKeySecret: 'xxxxx',
})

async function saveWallet(address: string, privateKey: string) {
  await locker.create({
    key: address,
    value: privateKey,
  })
}

async function getWallet(address: string) {
  const secretVal = await locker.get(address)
  return {
    address,
    privateKey: secretVal,
  }
}

async function listWallets() {
  const secrets = await locker.list()
  return secrets.map((secret) => ({
    address: secret.key,
    privateKey: secret.value,
  }))
}
