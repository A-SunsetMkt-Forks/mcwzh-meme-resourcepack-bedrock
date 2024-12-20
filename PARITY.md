# 与源项目保持同步

基岩版梗体中文源项目包括：

1. [`Teahouse-Studios/mcwzh-meme-resourcepack` （Java版梗体中文）](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack)
2. [`ff98sha/mclangcn` （基岩版译名修正）](https://github.com/ff98sha/mclangcn)。

## 与Java版梗体中文保持同步

基岩版梗体中文的内容应**实时**与Java版梗体中文保持同步。

基岩版的独有内容包括成就、游戏指南等。这些独有内容请不要只是进行简单替换，而应把整段的行文都梗化。

### 当您在Java版梗体中文提交了一次新的内容更新时

无论您是在Java版梗体中文提交议题（Issue）/拉取请求（Pull Request），还是直接进行提交的，都请在基岩版梗体中文进行一遍与其目的一致的操作。

请善用文字编辑器的搜索功能，找到基岩版梗体中文的语言文件（[`zh_ME.lang`](\meme_resourcepack\texts\zh_ME.lang)）中相应的字符串，将字符串内容更改至您提交至Java版梗体中文的语言文件（[`zh_meme.json`](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/assets/minecraft/lang/zh_meme.json)）的内容相一致即可完成同步。

反之亦然。

### 当两者长时间未保持同步时

通过Git可以查找到Java版梗体中文每一次的提交记录，可以清晰地看到更新的内容。

请善用文字编辑器的搜索功能，找到基岩版梗体中文的语言文件（[`zh_ME.lang`](\meme_resourcepack\texts\zh_ME.lang)）中对应的未同步内容。

接下来，找到基岩版语言文件（[`zh_ME.lang`](\meme_resourcepack\texts\zh_ME.lang)）中的相同字符串，将字符串内容更改至与Java版梗体中文的语言文件（[`zh_meme.json`](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/assets/minecraft/lang/zh_meme.json)）一致即可完成同步。

反之亦然（尽管这是完全不可能的）。

### 当两者无法完全同步时

除非需要同步的内容超出您的能力范畴，否则仍然需要同步。而有些内容由于版本受限，同步极其困难。

例如，Java版的OptiFine相关内容无法同步至基岩版（如[`BUGJUMP`](https://github.com/Teahouse-Studios/mcwzh-meme-resourcepack/blob/master/modules/BUGJUMP)），那就无需同步。

同理，基岩版的湖人蓝色UI模块（[`blue_ui`](\modules\blue_ui)）无法同步至Java版，也无需同步。

## 与基岩版译名修正保持同步

### 同步梗体中文的未梗化字符串

请妥善使用文字编辑器的比较和搜索功能，将梗体中文和译名修正的语言文件进行对比，缺失或不一致的字符串请及时进行增补和更改。

请注意，已经梗化过的字符串**无需**再和译名修正同步。

### 同步译名修正

梗体中文附带了一份译名修正（[`zh_CN.lang`](\meme_resourcepack\texts\zh_CN.lang)），只要从原仓库复制粘贴过来即可。

请记住第二行不要删去：

    ## Minecraft译名修正，来自ff98sha/mclangcn
