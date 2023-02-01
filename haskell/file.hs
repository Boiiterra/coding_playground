doubleMe :: Num a => a -> a
doubleMe x = x * 2

squareMe :: Num a => [a] -> [a]
squareMe a = [x * x | x<- a]

-- return difference between two arrays ( a and b )
arrayDiff :: Eq a => [a] -> [a] -> [a]
arrayDiff a b = [x | x <- a, x `notElem` b] ++ [x | x <- b, x `notElem` a]

boolInt :: Num p => Bool -> p
boolInt a = if a then 1 else 0

isVowel :: Char -> Bool
isVowel a = a `elem` ['a', 'e', 'i', 'o', 'u']

main :: IO()
main = do
    print $ doubleMe 2
    print $ arrayDiff [1, 2, 4, 4, 5] [1, 5, 6, 6] -- need to remove duplicates :D
    print $ sum $ squareMe [5, 3, 4]
    print $ 1 + boolInt True
    print $ isVowel 'a'