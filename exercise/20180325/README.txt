練習說明：

filelist.txt是一份SAS檔案清單，每一列(row)是一個包含Windows路徑的檔案名稱。
但其中也有些列只有一個數字，那些列可以忽略。

其中檔名以h_nhi_opdto開頭，後面帶有數字的檔案是"全民健保處方及治療醫令明細檔_門急診"(OO檔)，
例如 h_nhi_opdto10004_10.sas7bdat 是民國104年4月份的第一份檔案（一個月份有3個檔案）。

請寫一個程式清查：
1： 請將所有 h_nhi_opdto 的檔案挑出來輸出到另一個檔案，名稱為 oo_files.txt，
    去除路徑只輸出檔名，也是一列一個檔名。
2： 請在oo_files.txt的最後一列輸出最早與最晚的年度，格式為：
    最早＝民國 ？ 年，最後＝民國 ? 年

可能會利用到的程式內容：
* file IO 如 open, readlines, write, close 等
* string operation, string slice 等
* looping
* if





