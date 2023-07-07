#include <math.h>
#include <stdlib.h>

// 宣告全域變數
static double sum = 0.0;           // 計算數字總和
static double sum_squared = 0.0;   // 計算數字平方總和
static int32_t count = 0;          // 計算數字個數

// 計算標準差的函數
double get_stddev(int32_t number) {
  sum += number;                  // 更新數字總和
  sum_squared += pow(number, 2);  // 更新數字平方總和
  count++;                        // 更新數字個數

  if (count == 1) {               // 如果數字個數為1，返回0
    return 0.0;
  }

  double mean = sum / count;                    // 計算數字平均值
  double variance = (sum_squared - pow(sum, 2) / count) / (count - 1); // 計算方差
  double stddev = sqrt(variance);               // 計算標準差

  return stddev;
}

// 重置全域變數，清除輸入數字序列
void clear() {
  sum = 0.0;
  sum_squared = 0.0;
  count = 0;
}
