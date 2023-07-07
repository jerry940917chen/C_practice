#include <stdio.h>
#include <string.h>

#define MAX_LEN 1000 // 定義最大字串長度

int main() {
    char lyrics[MAX_LEN] = "I'm at a payphone trying to call home\nAll of my change I spent on you\nWhere have the times gone baby\nIt's all wrong, where are the plans we made for two?"; // 歌詞
    char *token, *str_ptr;
    char delim[] = " ,.\n";
    int word_count = 0;
    int index = 0;
    char words[MAX_LEN][MAX_LEN] = {0}; // 二維陣列，存儲歌詞中的每個單詞
    int word_index[MAX_LEN][MAX_LEN] = {0}; // 二維陣列，存儲每個單詞在歌詞中的位置
    int word_freq[MAX_LEN] = {0}; // 陣列，存儲每個單詞出現的次數
    
    // 將歌詞中的單詞存入 words 陣列，同時記錄每個單詞在歌詞中的位置
    str_ptr = lyrics;
    while ((token = strtok(str_ptr, delim))) {
        strcpy(words[word_count], token);
        word_index[word_count][word_freq[word_count]] = index;
        word_count++;
        word_freq[word_count - 1]++;
        index += strlen(token) + 1;
        str_ptr = NULL;
    }
    
    // 輸出每個單詞出現的次數
    for (int i = 0; i < word_count; i++) {
        printf("%s: %d\n", words[i], word_freq[i]);
    }
    
    return 0;
}