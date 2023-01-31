doubleMe :: Num a => a -> a
doubleMe x = x * 2

main :: IO()
main = do
    print $ doubleMe 2