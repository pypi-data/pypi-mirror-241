## QA
>QA is a tool for Android UI automated testing.

### Description
```bash
usage: qa [-h] [-v] {clear,info,adb,remote,proxy,unproxy} ...

QA is an advanced tool for Android testing! Created: Lijiawei. Version 0.0.8

positional arguments:
  {clear,info,adb,remote,proxy,unproxy}
                        sub-command help
    clear               clear app cache data.
    info                show app setting page.
    adb                 complete adb debugging capability.
    remote              open Android device remote debugging port(5555).
    proxy               enable device global proxy(172.17.30.10:8888).
    unproxy             disable device global proxy.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version


```

### Clear
> Clear app cache data
```bash
qa clear com.test.app
```

### Adb
> Complete adb debugging capability
```bash
qa adb
```

### Remote
> Open Android device remote debugging port(5555)
```bash
qa remote
```

### Proxy
> Enable device global proxy
```bash
qa proxy
```

### Unproxy
> Disable device global proxy
```bash
qa unproxy
```

### Info
> Show app info
```bash
qa info
```