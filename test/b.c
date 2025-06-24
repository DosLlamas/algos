#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(){
    int team1One, team1Two, team1Three;
    int team2One, team2Two, team2Three;
    scanf("%d%d%d", &team1One, &team1Two, &team1Three);
    scanf("%d%d%d", &team2One, &team2Two, &team2Three);
    int team1Total = team1One + team1Two*2 + team1Three*3;
    int team2Total = team2One + team2Two*2 + team2Three*3;
    if(team1Total > team2Total) printf("1");
    else if(team1Total < team2Total) printf("2");
    else printf("0");
    int t1;
    int t2;
    scanf("%d%d%d", &t1, (&t1)*2, (&t1)*3);
    scanf("%d%d%d", &t2, (&t2)*2, (&t2)*3);
    printf("%d", t1 > t2 ? 1 : t1 < t2 ? 2 : 0);
    return 0;
}