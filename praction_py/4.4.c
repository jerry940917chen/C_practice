#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
int32_t board[17][25];
bool done[17][25];
int32_t changey(int32_t x,int32_t y){
    if(0<=x && x<=3||(9<=x && x<=12)){
        return 12-x + 2*y;
    }
    if((4<=x && x<=8)||(13<=x && x<=16)){
        return x-4 + 2*y;
    }
}
void startplay(){
    for(int32_t i=0;i<17;i++){  //space
    	for(int32_t j=0;j<25;j++){
    	    board[i][j]=-1;
    	}
    }
    for(int32_t j=1;j<=4;j++){  //yellow
        for(int32_t i=0;i<j;i++){
            board[j-1][2*i+13-j]=1;
        }
    }
    for(int32_t j=0;j<=12;j++){ //white
        for(int32_t i=0;i<13-j;i++){
            board[j+4][2*i+j]=0;
        }
    }
    for(int32_t j=9;j<=12;j++){ //green
        for(int32_t i=0;i<j-8;i++){
            board[j][2*i+12-j]=2;
        }
    }
    for(int32_t j=9;j<=12;j++){ //red
        for(int32_t i=0;i<j-8;i++){
            board[j][2*i+30-j]=3;
        }
    }
    return;
}
void play(){
    for(int32_t i=0;i<17;i++){
    	for(int32_t j=0;j<25;j++){
            if(board[i][j]==-1){
                printf(" ");
            }
            else if(board[i][j]==0){
                printf("*");
            }
            else if(board[i][j]==1){
                printf("\e[38;5;220m*\e[m");
            }
            else if(board[i][j]==2){
                printf("\e[38;5;28m*\e[m");
            }
            else if(board[i][j]==3){
                printf("\e[38;5;124m*\e[m");
            }
    	}
        printf("\n");
    }
}
bool jump(int32_t fx,int32_t fy,int32_t tx,int32_t ty,int32_t hadJump){
    if(fx==tx && fy==ty && hadJump==1){
        return 1;
    }
    if(hadJump==1){
        done[fx][fy]=1;
    }
    int32_t space = 0;
    const int32_t move[6][2] = {{-1,-1},{-1,1},{0,-2},{0,2},{1,-1},{1,1}};
    for(int32_t i=0;i<6;i++){
        space=1;
        while((fx+space*move[i][0]<17) && (fx+space*move[i][1]>=0) &&
              (fy+space*move[i][0]<25) && (fy+space*move[i][1]>=0) && 
              (board[fx+space*move[i][0]][fy+space*move[i][1]]==0)){
            space++;
        }
        bool can=1;
        if(board[fx+space*move[i][0]][fy+space*move[i][1]]==-1){
            continue;
        }
        for(int32_t j=1;j<=space;j++){
            if((fx+(space+j)*move[i][0]>=17) || (fx+(space+j)*move[i][1]<0) ||
               (fy+(space+j)*move[i][0]>=25) || (fy+(space+j)*move[i][1]<0)){
                can=0;
                break;
            }
            if(board[fx+(space+j)*move[i][0]][fy+(space+j)*move[i][1]]!=0){
                can=0;
                break;
            }
        }
        if(can==1 && done[fx+2*space*move[i][0]][fy+2*space*move[i][1]]==0){
            if(jump(fx+2*space*move[i][0],fy+2*space*move[i][1],tx,ty,1)==1){
                return 1;
            }
        }
    }
    return 0;
}
bool check(int32_t fx,int32_t fy,int32_t tx,int32_t ty,int32_t player){
    if(board[tx][ty]!=0 && (fx!=tx || fy!=ty)){
        printf("Error,Please Enter Again!\n");
        return 0;
    }
    if(fx>17||fx<0||tx>17||tx<0||fy>25||fy<0||ty>25||ty<0){
        printf("Error,Please Enter Again!\n");
        return 0;
    }
    if(board[fx][fy] != player){
        printf("Error,Please Enter Again!\n");
        return 0;
    }
    if(fx==tx && fy+2==ty){
        return 1;
    }
    if(fx==tx && fy-2==ty){
        return 1;
    }
    if(fx==tx-1 && fy-1==ty){
        return 1;
    }
    if(fx==tx-1 && fy+1==ty){
        return 1;
    }
    if(fx==tx+1 && fy-1==ty){
        return 1;
    }
    if(fx==tx+1 && fy+1==ty){
        return 1;
    }
    for(int32_t i=0;i<17;i++){
        for(int32_t j=0;j<25;j++){
            done[i][j]=0;
        }
    }
    board[fx][fy] = 0;
    if(jump(fx,fy,tx,ty,0)==1){
        board[fx][fy] = player;
        return 1;
    }
    board[fx][fy] = player;
    printf("Error,Please Enter Again!\n");
    return 0;
}
bool checkWin(int32_t player){
    bool win=1;
    if(player==1){
        for(int32_t i=13;i<=16;i++){
            for(int32_t j=0;j<17-j;j++){
                if(board[i][changey(i,j)]!=1){
                    win=0;
                    break;
                }
            }
            if(win==0){
                break;
            }
        }
        if(win==1){
            return 1;
        }
    }
    win=1;
    if(player==2){
        for(int32_t i=4;i<=7;i++){
            for(int32_t j=0;j<17-j;j++){
                if(board[i][changey(i,j+9)]!=2){
                    win=0;
                    break;
                }
            }
            if(win==0){
                break;
            }
        }
        if(win==1){
            return 1;
        }
    }
    win=1;
    if(player==3){
        for(int32_t i=4;i<=7;i++){
            for(int32_t j=0;j<17-j;j++){
                if(board[i][changey(i,j)]!=3){
                    win=0;
                    break;
                }
            }
            if(win==0){
                break;
            }
        }
        if(win==1){
            return 1;
        }
    }
    return 0;
}
int main(){
    startplay();
    int32_t fx=0,fy=0,tx=0,ty=0;
    while(1){       
        do{
            play();
            printf("Yello Player turn: \n");
            printf("  From: ");
            scanf("%d,%d",&fx,&fy);
            printf("  To: ");
            scanf("%d,%d",&tx,&ty);
            fy = changey(fx,fy);
            ty = changey(tx,ty);
        }while(check(fx,fy,tx,ty,1)==0);
        board[tx][ty] = board[fx][fy];
        if(fx!=tx || fy!=ty){
            board[fx][fy] = 0;
        }
        if(checkWin(1)==1){
            printf("The Winner is Yellow\n");
            return 0;
        }
        do{
            play();
            printf("Green Player turn: \n");
            printf("  From: ");
            scanf("%d,%d",&fx,&fy);
            printf("  To: ");
            scanf("%d,%d",&tx,&ty);
            fy = changey(fx,fy);
            ty = changey(tx,ty);
        }while(check(fx,fy,tx,ty,2)==0);
        board[tx][ty] = board[fx][fy];
        if(fx!=tx || fy!=ty){
            board[fx][fy] = 0;
        }
        if(checkWin(2)==1){
            printf("The Winner is Green\n");
            return 0;
        }
        do{
            play();
            printf("Red Player turn: \n");
            printf("  From: ");
            scanf("%d,%d",&fx,&fy);
            printf("  To: ");
            scanf("%d,%d",&tx,&ty);
            fy = changey(fx,fy);
            ty = changey(tx,ty);
        }while(check(fx,fy,tx,ty,3)==0);
        board[tx][ty] = board[fx][fy];
        if(fx!=tx || fy!=ty){
            board[fx][fy] = 0;
        }
        if(checkWin(3)==1){
            printf("The Winner is Red\n");
            return 0;
        }
    }
    return 0;
}