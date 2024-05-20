# 2018
**투 포인터 이동 원칙**
- `sum` > `N` 
    `sum` = `sum` - `start_index` , `start_index++`
- `sum` < `N`
    `end_index++` , `sum` = `sum` + `end_index` 
- `sum` == `N`
    `end_index++`, `sum` = `sum` + `end_index` , `cnt++`
