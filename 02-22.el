(defun rps-score ()
  "Calculate score of rock paper scissors"
  (interactive)
  (replace-regexp "A X" "4")
  (goto-char (point-min))
  (replace-regexp "A Y" "8")
  (goto-char (point-min))
  (replace-regexp "A Z" "3")
  (goto-char (point-min))
  (replace-regexp "B X" "1")
  (goto-char (point-min))
  (replace-regexp "B Y" "5")
  (goto-char (point-min))
  (replace-regexp "B Z" "9")
  (goto-char (point-min))
  (replace-regexp "C X" "7")
  (goto-char (point-min))
  (replace-regexp "C Y" "2")
  (goto-char (point-min))
  (replace-regexp "C Z" "6"))
; A for Rock, B for Paper, and C for Scissors
; X for Rock, Y for Paper, and Z for Scissors
; 1 for Rock, 2 for Paper, and 3 for Scissors
; 0 if you lost, 3 if the round was a draw, and 6 if you won


