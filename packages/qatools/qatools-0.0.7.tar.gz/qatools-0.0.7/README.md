## QA
>QA is a tool for Android UI automated testing.

### Description
```bash
usage: qa [-h] [-v] {clear,adb,remote,proxy,unproxy} ...

UTX will help you write ui automated tests more easily! Created: Lijiawei. Version 0.0.1

positional arguments:
  {clear,adb,remote,proxy,unproxy}
                        sub-command help
    clear               clear app cache data).
    adb                 complete adb debugging capability.
    remote              open Android device remote debugging port(5555).
    proxy               enable device global proxy(172.1.0.3:8888).
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