# Log 解析
處理 JSON 格式的 log 檔 (檔案依老師指定)，針對各服務計算不同嚴重等級 log 次數，共計 3 個任務

## 任務 1  
**針對每個服務 (服務名稱記錄在 "service_name") 計算並輸出各種嚴重等級(嚴重等級記錄在 "severity") log 發生的次數於螢幕，格式不限，順序不限**

### 限制
> 1. 允許被 import 的套件限於 json 與 os，禁止 import 其他套件
> 2. 服務名稱與嚴重等級不得寫死，亦即，程式碼不能含 "pauca"、"myca"、"wt"、"ERROR"、"INFO"、"NOTICE"、"WARNING" 等常數

### 輸出內容
```text
pauca ERROR: 26/ INFO: 23/ NOTICE: 0/ WARNING: 2
myca  ERROR:  0/ INFO:  3/ NOTICE: 0/ WARNING: 0
wt    ERROR: 36/ INFO: 53/ NOTICE: 1/ WARNING: 0
```

## 任務 2  
**將任務 1 包裝為 function，能夠指定待處理的 log 檔名，並於螢幕輸出所有服務各種嚴重等級次數**

### 限制
> 1. 允許被 import 的套件限於 json 與 os，禁止 import 其他套件
> 2. 輸出格式須遵循下列 "輸出內容" 範例 (須特別注意對齊與空白)，其中嚴重等級依字母順序，但服務名稱無順序
> 3. 服務名稱與嚴重等級不得寫死，亦即，程式碼不能含 "pauca"、"myca"、"wt"、"ERROR"、"INFO"、"NOTICE"、"WARNING" 等常數
> 4. Log 檔名不得寫死，亦即，程式碼不含 "serviceslogs.json" 等常數
> 5. Function 須防呆 & 容錯，亦即，function 的執行不能因參數值的任意設定導致例外而中斷

### 輸出內容
```text
pauca ERROR: 26/ INFO: 23/ NOTICE: 0/ WARNING: 2
myca  ERROR:  0/ INFO:  3/ NOTICE: 0/ WARNING: 0
wt    ERROR: 36/ INFO: 53/ NOTICE: 1/ WARNING: 0
```

## 任務 3  
**強化任務 2 function，除能夠指定待處理的 log 檔名，預設能夠於螢幕輸出所有服務各種嚴重等級次數 (效果同任務2)，亦能夠僅輸出指定服務的各種嚴重等級次數，或輸出至指定檔案**

### 限制
> 1. 允許被 import 的套件限於 json 與 os，禁止 import 其他套件
> 2. 輸出格式須遵循下列 "輸出內容" 範例 (須特別注意對齊與空白)，其中嚴重等級依字母順序，但服務名稱無順序
> 3. 服務名稱與嚴重等級不得寫死，亦即，程式碼不能含 "pauca"、"myca"、"wt"、"ERROR"、"INFO"、"NOTICE"、"WARNING" 等常數
> 4. Log 檔名不得寫死，亦即，程式碼不含 "serviceslogs.json" 等常數
> 5. Function 須防呆 & 容錯，亦即，function 的執行不能因參數值的任意設定導致例外而中斷

### 輸出內容
```text
wt ERROR: 36/ INFO: 53/ NOTICE: 1
```

## 注意事項
> 1. 禁止 vibe coding，違者總分 0 分
> 2. 禁止抄襲，違者總分 0 分
> 3. 允許被 import 的套件限於 json 與 os，禁止 import 其他套件，違者該任務 0 分
> 4. 服務名稱與嚴重等級不得寫死，違者該任務 0 分
> 5. 注意任務 2 & 任務 3 要求的包裝方式為 function；若包裝為 class 則該任務 0 分
> 6. 評分時將以同規格的其他服務 log 檔驗證，須注意輸出數據正確性與輸出整齊度
> 7. 注意 "service_name" 非 "serviceName"
> 8. 以 Jupyter Notebook 開發的同學交卷前務必將各任務 Restart Kernal 後執行一遍確認程式執行符合預期
> 9. 任務 2 & 任務 3 不須準備叫用範例
> 10. 允許只繳交任務 3，但若任務 3 出現嚴重失誤可能導致任務 1 與任務 2 的評分為 0 分

## 評分標準  
| 項目 | 總佔比 | 任務 1 | 任務 2 | 任務 3 |
| :--- | ---: | ---: | ---: | ---: |
| 正確運作 | 60% | 30% | 20% | 10% |
| 程式邏輯與效率 | 30% | 10% | 10% | 10% |
| coding style | 10% | 4% | 3% | 3% |
| docstring 描述解題邏輯與心得 | +20% ||||

## 交卷方式
|||
| :--- | :--- |
| email | catchsob@gmail.com |
| 時間 | **2026/09/22-23:59:59 前，逾時總分 0 分**；任何問題導致交卷失敗總分 0 分。可以重複交卷，老師只批改有效時間內的最後一次交卷內容。老師預計在 2026/09/22-22:00 與 2026/09/23-00:02 於 LINE 社群 (GAE265 x Enos老師：商務AI應用開發人才養成班第02期) 公告交卷同學座號 |
| 主旨 | GAE265 Python 測驗 03 王大同 |
| 內容 | as title |
| 夾檔 | GAE265_03_王大同.py or GAE265_03_王大同.ipynb |
