# Question 1
- hashet-earlier uses sha1
- hash-bad uses md5
- hash-good uses sha256


# Question 2
<code>
  sha1sum -c hashset-earlier
</code>

sha1sum computation fails for following files:

- f0022
- f0148
- f0254
- f0261
- f0407
- f0478


# Question 3
<code>
  sha1sum -c hashset-earlier
</code>

these files are deleted as they sha1sum fails to open them:

- f0128 failed to open
- f0258 failed to open
- f0480 failed to open
- f0490 failed to open


# Question 4
<code>
  sort -k1 hashset-earlier | rev | uniq -D -f1 | rev
</code>

- 0394531ea5da00dbc3952596ce4dfd053fab9ea0  f0063 and f0462  
- 4898178118fd5b7f058ee965f9e0e38c63a37c3a  f0098, f0127, f0153 and f0155  
- 5894bb804be6cdef4821117033132899131d7515  f0288 and f0458
- b399dfae40356cb84560f242dacae11070afc038  f0081 and f0161
- b4ed696c59f5c71f238d12df568f4611d9d0a4d7  f0064 and f0144
- ba9243a005098d670b83a1a3013ed6f46f15853c  f0315 and f0471


# Question 5
<code>
  sha1sum --check * 2>/dev/null | grep 'FAILED open or read' | cut -d ":" -f1 > missingfiles; grep -f missingfiles hashset-earlier | cut -d " " -f1 > missinghashes; sha1sum * | grep -f missinghashes
</code>

Stupid method that I have used is, check hashes of the files that are not found, are they present in hashet-earlier

- f0480 is renamed to f0478


# Question 6
<code>
  md5sum * > md5original
</code>
</br>
<code>
  grep -f hashset-bad md5original
</code>

- b14f4aa8fc562a11fad70d2b5dbcf27a  f0012
- d9a1399c2f017ecc771a6ac412acf5ec  f0035
- 74b336ad0f10d1c5dec68d1161af86b7  f0097
- 71e8af818f4e80d13af1124930e13260  f0135
- 70fbee7a870e90156f7f61de47e0d4be  f0147
- 4dba5d3955a842581f8ccb42216650d3  f0191
- 4d042a18cb71f2396b958f42257e44f3  f0233
- f099963c11fed01a88d4a1ab142b1eae  f0239
- d4cec7a9f0a275e15a4dce03f71a397a  f0328
- db402049b23fff31d0091512efb02ceb  f0353
- 6babb0d4d500e2bea9f8c4805c2ed5a7  f0398
- 4f36d7c140f9797a599abe3282b9b1b4  f0482
- ec0a2f22305494f6a4754e68710df04d  f0496


# Question 7
<code>
  grep -vf hashset-bad md5sum > notmalware; grep -vf hashset-good sha256sum > notgood; grep -vf notmalware notgood
</code>

- 4d66fe7f15c4ca119e7a1a5e9cead03d238c052e068b853146cc0f677c5057b8  f0012
- 300cfae66d0d0ab27e6b0c97766a7834622adf2015d19897a6dfda05c3809df7  f0022
- 62ed26ccbccc6187f1ef6d9704595995ac7c05395f1700624de86e72cf575c83  f0035
- 2694fcbd64ef9da3e9fee05d8c5a3e31457097d07b3af8dbd9d79ca3238374f7  f0050
- 219b7751833868d48e763366973a453312a64d1a1a0cd1f65a89b689e1b8ecc5  f0096
- 2b405fe96aa4914a3e93b76760ab4131569f85e6a2548b74e18fbadf9891904a  f0097
- 4be69830438f0b2bff66e37ffb1ac3dc922a819da7a643998300b803ce8d4730  f0119
- 817dd3ab72c765a11be9fe81f3f1d722286d4ce3d6b20cf5d90a66476591bd52  f0135
- 860ea8afa21ff5767494b87615ec5bbf73b2be88b1952b83c23616568118f47a  f0142
- f78bcdcde0f672c92175bac0d1090e0e4e40aca0b94306967d3c83d28af5c9a9  f0147
- 1fc8f4949c02a39fdd7b850e9a6117e81d899eb32c4c943d104414ee539733d5  f0148
- 16373c33e12a07ca77c2da37e52832acee89660affe3ee5936b23eed9233c7d2  f0171
- 89ebc04ee18bd149387c1944ab1fbb7f1dea1ed6b33021d3e2ab27649f9524ca  f0191
- 0038f28e617f350e1f42297887bbb39c2a546d9b401107778ff05d41a32a2093  f0213
- 8c0806258be2ca18c67a3ce3389883a9b9a6d2380108cf52e2aa7fc10eb1bcba  f0233
- f25239ccf64cf1d81eafd00a65fae31621ac77aa1172db1678b9e9423f033d56  f0239
- ef990e3bc617df32eed7f29beaf0c7024f4ce91545590c0f231fe6a6c4fc0e52  f0254
- bb51f8c3d42aec5182c90c6ba932193b7ff052eae015093499405b1b76b995b4  f0261
- 053eec3a0848515aefe84906a708636faff9a73d659249679dd9c89bf344be89  f0328
- f536ea54fb51fff51197882e7602fd4ca5eae6e5418f02270d76216e4893ab2c  f0353
- 3828dde81f5e46f6d7f94ffd12e72f5109ba4a66b22bd707e98ac6ae80cf5a3c  f0362
- d32af28556e6c38ebc16f9bbe9197852393b985fd5896a5d5fe0942edc22e40f  f0394
- fc3fb6085bea3d6e24ee25aa8ae496016044e54ca9375e33fcf214e25a1e7758  f0398
- 2b17790e6922af193568d2d77a9b4f8a661d52c07152b6bedfbeb1f762a77ade  f0407
- c502ff9e1261383c6893b3bae5a91f8b94e13ab3065ee7103496eb8d5f84d655  f0410
- 43e46e18bd3eb1eee5ea13231dc18b60b090b4bde09fc7b3919c553bd28c51e7  f0467
- bb002de9ab70b4da03dc81cfe2228be5971d313340278aee4650974774a660f4  f0482
- 055f1bbb23727b64060b9b7fc2fec662c9c547bda372317dfbaf7d59dfa4dbd9  f0489
- be81694ce29158e2b11e94e30e2b519b322e0b5eadce582ba486a3034119519d  f0493
- 0fcfb3f36601817adb78b9d4ccae60b64eeec213a6b955bcb5a8bdc5a2c26caa  f0496
