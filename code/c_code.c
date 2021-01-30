for (int i = 0; i < 1000; i++) {
    int list = malloc(1000000 * sizeof(int));
    for (int j = 0; j < 1000000; j++) {
        list[j] = j;
    }
    free();
}