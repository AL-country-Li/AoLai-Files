# F1:
```c++
#include <iostream>

int main() {
    const char *s =
        "#include <iostream>%c"
        "%c"
        "int main() {%c"
        "    const char *s =%c"
        "        %c%s%c;%c"
        "%c"
        "    char q = 34;%c"
        "%c"
        "    for (const char *p = s; *p; ++p) {%c"
        "        if (*p == '%') {%c"
        "            ++p;%c"
        "            if (*p == 'c') std::cout.put(10);%c"
        "            else if (*p == 's') {%c"
        "                std::cout << q;%c"
        "                for (const char *t = s; *t; ++t) {%c"
        "                    if (*t == 10) std::cout << %c\\\\n%c;%c"
        "                    else if (*t == 92) std::cout << %c\\\\\\\\%c;%c"
        "                    else if (*t == 34) std::cout << %c\\\\%c%c;%c"
        "                    else std::cout << *t;%c"
        "                }%c"
        "                std::cout << q;%c"
        "            }%c"
        "        } else {%c"
        "            std::cout << *p;%c"
        "        }%c"
        "    }%c"
        "}";

    char q = 34;

    for (const char *p = s; *p; ++p) {
        if (*p == '%') {
            ++p;
            if (*p == 'c') std::cout.put(10);
            else if (*p == 's') {
                std::cout << q;
                for (const char *t = s; *t; ++t) {
                    if (*t == 10) std::cout << "\\n";
                    else if (*t == 92) std::cout << "\\\\";
                    else if (*t == 34) std::cout << "\\\"";
                    else std::cout << *t;
                }
                std::cout << q;
            }
        } else {
            std::cout << *p;
        }
    }
}
```
# F2:
```c++
#include <iostream>
#include <string>

void print_escaped(const std::string& s) {
    for (char c : s) {
        switch (c) {
            case '\n': std::cout << "\\n"; break;
            case '\\': std::cout << "\\\\"; break;
            case '\"': std::cout << "\\\""; break;
            default:   std::cout << c;
        }
    }
}

int main() {
    std::string s = 
"#include <iostream>\n#include <string>\n\nvoid print_escaped(const std::string& s) {\n    for (char c : s) {\n        switch (c) {\n            case '\\n': std::cout << \"\\\\n\"; break;\n            case '\\\\': std::cout << \"\\\\\\\\\"; break;\n            case '\\\"': std::cout << \"\\\\\\\"\"; break;\n            default:   std::cout << c;\n        }\n    }\n}\n\nint main() {\n    std::string s = \n\"@\";\n    std::string pre = s.substr(0, s.find('@'));\n    std::string post = s.substr(s.find('@') + 1);\n    std::cout << pre;\n    print_escaped(s);\n    std::cout << post;\n}\n";
    std::string pre = s.substr(0, s.find('@'));
    std::string post = s.substr(s.find('@') + 1);
    std::cout << pre;
    print_escaped(s);
    std::cout << post;
}
```
# F3:
```c++
#include <cstdio>
int main(){const char*s="#include <cstdio>%cint main(){const char*s=%c%s%c;printf(s,10,34,s,34,10);}";printf(s,10,34,s,34,10);}
```
附：OOP为面向对象编程