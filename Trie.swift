import Foundation

class TrieNode<T: Hashable> {
    var value: T?
    weak var parent: TrieNode?
    var isTerminating = false
    var children : [T: TrieNode] = [:]
    
    init(value: T? = nil, parent: TrieNode? = nil) {
        self.value = value
        self.parent = parent
    }
    
    func add(child: T) {
        guard children[child] == nil else { return }
        
        children[child] = TrieNode(value: child, parent: nil)
    }
}

class Trie {
    typealias Node = TrieNode<Character>
    fileprivate let root : Node
    
    init() {
        root = Node()
    }
    
    func Insert(word: String) {
        guard !word.isEmpty else { return }
        
        var currentNode = root
        
        let characters = Array(word.lowercased().characters)
        var currentIndex = 0
        
        while currentIndex < characters.count {
            let character = characters[currentIndex]
            
            if let child = currentNode.children[character] {
                currentNode = child
            } else {
                currentNode.add(child: character)
                currentNode = currentNode.children[character]!
            }
            currentIndex += 1
        }
        currentNode.isTerminating = true
    }
    
    func Contains(word: String) -> Bool {
        guard !word.isEmpty else { return false}
        
        var currentNode = root
        let characters = Array(word.lowercased().characters)
        var currentIndex = 0
        while currentIndex < characters.count , let child = currentNode.children[characters[currentIndex]] {
            
            currentIndex += 1
            currentNode = child
        }
        if currentIndex == characters.count && currentNode.isTerminating {
            return true
        }
        return false
    }
    
    func findMax() -> String {
        
    }
}


let trie = Trie()
let file = "wordsforproblem.txt" //this is the file. we will write to and read from it


if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
    
    let path = dir.appendingPathComponent(file)
    print(dir)
    //reading
    do {
        let data = try String(contentsOf: path, encoding: String.Encoding.utf8)
        let content = data.components(separatedBy: .newlines)
        for word in content {
            trie.Insert(word: word)
        }
    }
    catch {/* error handling here */}
}

print(trie.findLogest())

