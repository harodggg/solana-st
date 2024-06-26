# solana-st

## 1. Install solana python sdk / js sdk / cargo sdk
```bash
npm install --save @solana/web3.js
pip3 install solders
pip3 install solana
cargo add solana-program
```

## 2. solana account model
![Alt text](image.png)

## 3. solana account info 
![Alt text](image-1.png)

## 4. program account and data account 
![Alt text](image-2.png)

## 5. delete a data account program
[delete-account program](delete-account)

## 6. Serialization scheme
1. packet
2. bincode
3. borsh

## 7. BPF--Berbeley-Packet-Filter
BPF 一种虚拟字节码，需要运行在虚拟机上
rust 编译BPF字节码
```bash
cargo build-bpf
```

solana 部署BPF字节码
```bash
 solana program deploy ./hello_world/target/deploy/hello_world.so 
```
solana 关闭程序账户
```bash
solana program close DsF7XpSZZv4hqcFqHpVowf6UPPkdjvDmhdFtDzifE9qp --bypass-warning
```

## 8. PDA--(program-dervie-account)
![Alt text](image-4.png)
![Alt text](image-5.png)
![Alt text](image-6.png)
1. PDA 账户是公开透明的
2. PDA 账户是被找出来的，通过程序id/自己拥有地址 + bump(0~255) + 可选的(seed)
3. PDA 账户的创造者可以对PDA账户进行签名
4. PDA 账户的拥有者可以对账户数据进行修改
5. PDA 调用合约，使用invoke_signed(),普通账户调用使用invoke()


## 9. 一些最初期的尝试，包含错误
![Alt text](image-3.png)

## 10. POH--(proof-of-history)
![Alt text](image-9.png)

1. base on vdf
2. 并不是确定性时间协议，而是确定时间发生顺序的协议
3. 上一次输出，作为下一次输入，不断的在单核内一直执行
4. 如果想要破坏，就必须要从头开始生成hash
5. 计算机的生成hash的速度是有限
6. 如果重新生成hash 就错过了slot时间导致交易无效

## 11. CPI (cross-program-interface)
1. 4个深度( A调用B-> C -> D)
2. 基于PDA


## 12. bytesTobase58
[keypair](bytesTobase58.py)

## 13. createmanyaccount
[create_wallet](create_wallet.py)

## 14. rent
1. There is a rent fee to create a new account
2. If the sol address balance meets the rent fee for 2 years, it will be free
3. The rent fee is charged at the end of the epoch, which takes about 2 days per epoch. Or when this address initiates a transaction on the chain.
4. If the sol is insufficient to pay the rent fee, the account will be deleted.
5. data > 0, each byte will be charged a rent fee, which is about 10M for ordinary accounts and about 10K for program accounts.

## 15. account with seed
通过seed，可以用同一个密钥建立多个不同的地址

## 16. nonce account
1. 离线交易和签名
2. 并发交易

## 17. stake account
1. 委托

## 18. tower BFT
![Alt text](image-7.png)
![Alt text](image-8.png)
![bft](https://assets-global.website-files.com/641ba798c17bb180d832b666/65a9aa2b9d3d3a0b3ccf7bc9_tNaLa5UPrg-gtH7Tn9O1gtLnR_hQMh75sTWLeaMOHezvdCSerpc4LcggL4btBTOh4_oh1VIZfVCd1QgGLlHIJnHXPVAnij0TGQej7m0Oexk0LpLrL-PfWhe2mZ_iMVgYvzsoIarhZcngMFkKTChtAPY.jpeg)

1. leader 选取一个epoch(2天到3天)
2. leader 选取是根据投票权重随机选取的
3. leader 在出块的时候，会同时分配4个slot,每一个slot的时间是400ms, 4个1.6s
4. 必须创造一系列POH刻度
5. 每一个区块的诞生必须要符合POH 在规定的slot内

## other restore resources
1. https://solana-asset-recovery.vercel.app/account


## solana devent/testnet faucet
1. https://faucet.solana.com/
2. https://solfaucet.com/
3. https://dev-faucet.solanahub.app/
4. https://faucet.quicknode.com/solana/devnet
5. https://stardust-solana-faucet.vercel.app/

## solana rpc
1. https://api.devnet.solana.com
2. https://api.testnet.solana.com






