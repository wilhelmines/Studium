double k = 1;
double s = 0;

int timeout = 10;   // [seconds]

// timeout_start = time.time()

while (timeout > 0) {
    double s_temp = 1 / k;
    double k++;
    double s += s_temp;
    printf(s);
}