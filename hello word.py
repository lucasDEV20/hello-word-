def hello_multiverse():
    # Dicionário com a sintaxe de cada linguagem
    helloworlds = {
        "Python": 'print("Hello, World!")',
        "JavaScript": 'console.log("Hello, World!");',
        "Java": 'System.out.println("Hello, World!");',
        "C++": 'std::cout << "Hello, World!";',
        "PHP": 'echo "Hello, World!";',
        "Ruby": 'puts "Hello, World!"',
        "Go": 'fmt.Println("Hello, World!")',
        "Rust": 'println!("Hello, World!");',
        "Swift": 'print("Hello, World!")',
        "SQL": "SELECT 'Hello, World!';"
    }

    print("--- 🌍 Hello World em várias linguagens ---")
    
    for lang, code in helloworlds.items():
        # Alinha o texto para ficar bonitão no terminal
        print(f"{lang.ljust(12)} | {code}")

if __name__ == "__main__":
    hello_multiverse()v