// yarn add lockerpm

const lockerpm = require('lockerpm')

const locker = new lockerpm.Locker({
  accessKeyId: 'xxxx',
  accessKeySecret: 'xxxxx',
})

async function saveWallet(address, privateKey) {
  await locker.create({
    key: address,
    value: privateKey,
  })
}

async function getWallet(address) {
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

async function test() {
  const address = '0x000'
  await saveWallet(address, '123123123')
  const wallet = await getWallet(address)
  console.log(wallet)
}

test()
