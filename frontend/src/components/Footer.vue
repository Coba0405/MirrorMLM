<template>
  <footer class=" text-gray-900 py-12 px-6">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 shadow-md">

      <!-- 左カラム：説明 -->
      <div class="space-y-6 text-left">
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          ボーナス金額は<br>「グループBV × ボーナス利率 − ダウンへのディストリビューション」で算出。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          ダウン人数の増加率は
          <a
            href="https://www.iieej.org/public/committees/ssc/confs/ssc3/ssc3-2.pdf"
            target="_blank"
            class="text-blue-400 hover:underline"
          >
            SSC研究報告書
          </a>
          に基づき、5%を前提とし算出。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          一人加入毎にグループPVに360,000PVが加算。
        </p>
        <p class="text-sm leading-relaxed text-gray-800 border-l-4 border-blue-400 pl-4">
          加入後2ヶ月は継続率100%、以降は年間30%の退会を想定。
        </p>
      </div>

      <!-- 右カラム：費用・注意 -->
      <div class="space-y-6 text-left">
        <div class="text-sm text-gray-800 space-y-2 border-l-4 border-blue-400 pl-4">
          <span>活動費：地域ごとに設定</span>
          <p>（一人当たりの勧誘費 + 一人当たりの交通費）× 勧誘人数月間のイベント費</p>
          <ul class="list-disc list-inside">
            <li>都心部：(¥1,200 + ¥500) × 勧誘人数 + ¥10,000</li>
            <li>地方都市：(¥1,000 + ¥300) × 勧誘人数 + ¥5,000</li>
            <li>地方：(¥900 + ¥200) × 勧誘人数 + ¥4,000</li>
          </ul>
        </div>

        <div class="text-sm text-gray-800 border-l-4 border-blue-400 pl-4">
          純利益 = ボーナス − 購入金額 − 活動費
          <br /> ※ 青背景の行が「純利益あり」の月です。
        </div>

      </div>
    </div>

    <!-- コピーライト -->
    <div class="mt-12 text-center text-xs text-gray-500 border-t border-gray-700 pt-4">
      <p class="text-xs text-gray-500 pt-4">
        このシミュレーターは参考情報であり、実際の報酬・費用とは異なる場合があります。個別の投資判断は自己責任でお願いいたします。
      </p>
      © 2025 MirrorMLM. All rights reserved.
    </div>
  </footer>
</template>