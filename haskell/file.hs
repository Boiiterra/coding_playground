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

cool a = init $ tail a

main :: IO()
main = do
    print $ doubleMe 2
    print $ arrayDiff [1, 2, 4, 4, 5] [1, 5, 6, 6] -- need to remove duplicates :D
    print $ sum $ squareMe [5, 3, 4]
    print $ 1 + boolInt True
    print $ isVowel 'a'

    print $ replicate 5 1
    print $ [x | x <- [50..100], x `mod` 7 == 0]

    print "Some triangles:"
    print $ [(a, b, c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2]
    print "End of some triangles."

    print $ minimum [1,2,1,2,3,4,5,6,4,5,6,5,0,6,5,7,9,1,2,4,9,7,4,6,5]

