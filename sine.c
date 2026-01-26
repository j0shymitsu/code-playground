#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

int main()
{
  for (double i = 1.0; i < 10000.0; i += 0.2)
  {
    int pos = 40 + 40 * sin(i);
    printf("%*s*\n", pos, "");
    usleep(50000);
  }
  printf("\n");

  return 0;
}