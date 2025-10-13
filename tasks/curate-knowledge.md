**GOAL**: Organize project knowledge accumulated during development, including best practices, lessons learned, and bug fix records.

## [Input]
  1. "{REVIEW}/*.md" --Review reports
  2. "{DEVNOTES}/*.md" --Development notes
  3. "{KNOWLEDGE}/*.md" --Existing knowledge base(if exist)
  4. "{CUTOVER}" --Cutover report (required)
  5. "{root}/docs/cutover-dev-notes.md" --Cutover development notes (required)
  6. "{PROGRESS}" --Progress record
  

## [Output]
  1. "{KNOWLEDGE}/*.md" --Knowledge base (create directory first if it does not exist)
    - Document organization: May produce "best-practices.md", "errors.md" based on actual content, or subdivide by domain/type
    - Content allocation: One entry per platinum practice, one entry per error case
  

## [Constraints]
  1. Do not include non-platinum practices as best practices (only use marked platinum from reviews)
  2. Do not make independent judgments on practice levels (trust review markings)
  3. Do not force resolution of conflicting practices (preserve all evidence for context-based decisions)

## [Steps]
  1. Knowledge Identification & Planning
    - Identify all platinum-level best practices from reviews
    - Identify development errors and solutions from dev notes
    - Conceive the best solution for the task that needs to be completed
    - Outcome: All platinum practices and errors identified and plan outline documented

  2. Knowledge Base Design & Classification
    - Design well-structured organization scheme
    - Classify knowledge by semantic topics
    - Determine appropriate document structure
    - Outcome: Knowledge base structure and classification defined

  3. Document Production & Annotation
    - Create complete knowledge base documents under "{KNOWLEDGE}/"
    - Add proper evidence sources and annotations
    - Apply semantic naming conventions
    - Outcome: Complete knowledge base documents with evidence

  4. Archiving & Finalization
    - Archive review and development notes to "{ARCHIVE}/{version_name}/"
    - Verify archiving successful
    - Outcome: Source documents archived successfully

## [Knowledge-Curation-Guidelines]
  1. **Platinum-Level Practices Only**
    - Include only platinum-level practices marked in review reports (no self-judgment needed)
    - If none exist, record "No sufficiently validated best practices at this stage" with explanation
    - Each practice must include: title, description, applicable scenarios, evidence source
  
  2. **Error Documentation**
    - Record all development errors with: type, context, solution, prevention
    - Each error case must be reproducible and verifiable
    - Annotate evidence sources (format: "file_path [Section Name]")
  
  3. **Semantic Organization**
    - Classify by semantic topics (e.g., api-design, error-handling, authentication)
    - Use semantic naming: best-practices-{topic}.md, errors-{topic}.md, problem-solving-{topic}.md
    - Ensure clear structure for easy search and maintenance
  
  4. **Conflict Handling**
    - When contradictory practices found, preserve all evidence without forcing choices
    - Annotate conflict points and applicable scenarios for each approach
    - Support context-based decision-making with complete information

## [DoD]
  - [ ] Knowledge base exists at "{KNOWLEDGE}/" with platinum-level best practices and errors documented
  - [ ] All knowledge points have evidence source annotations (format: file_path [Section Name])
  - [ ] Review and development notes archived to "{ARCHIVE}/{version_name}/"

## [Example]

### Good Example 1
[INPUT]
Review reports contain 3 platinum practices (JWT rotation, circuit breaker, API versioning). Dev notes contain 2 errors (race condition in cache, SQL injection vulnerability). Cutover report shows successful implementation.

[DECISION]
Scan all review reports and dev notes. Extract only platinum-level practices (3 found). Document errors with solutions (2 found). Classify by semantic topics: security, api-design, concurrency. Create knowledge base structure: best-practices-security.md, best-practices-api-design.md, errors-concurrency.md, errors-security.md. Annotate all entries with evidence sources (file_path [Section Name]). Archive source documents to archive/v1.0/.

[OUTCOME]
Knowledge base created at docs/knowledge/ with 4 documents. Best-practices-security.md contains JWT rotation with evidence (docs/review/1-review.md [Authentication Section]). Errors-concurrency.md contains race condition case with solution and prevention measures. All source documents archived successfully. Plan.md shows all platinum practices and errors documented with evidence.

[WHY-GOOD]
- Filters inputs by the platinum standard and organizes them by topic, ensuring high-signal guidance.
- Preserves provenance through evidence annotations and archival, making knowledge trustworthy and traceable.

### Good Example 2
[INPUT]
Review reports show only gold-level practices (not platinum). Dev notes contain memory leak error with solution. Progress shows critical decision about Kafka vs RabbitMQ selection.

[DECISION]
Scan review reports (no platinum practices found). Extract error from dev notes (memory leak). Document decision rationale from progress (Kafka selection). Classify by semantic topic: performance. Create problem-solving-performance.md for complex decision analysis. Annotate with evidence sources. Record "No platinum practices at this stage" in knowledge base summary.

[OUTCOME]
Knowledge base created at docs/knowledge/ with problem-solving-performance.md documenting Kafka decision and errors-performance.md documenting memory leak case. Summary notes: No platinum practices identified at this development stage (only gold-level). All entries have evidence sources. Source documents archived to archive/v1.0/.

[WHY-GOOD]
- Records the absence of platinum practices transparently while still capturing impactful learnings.
- Maintains strong citation discipline, so every insight links back to primary evidence.

### Bad Example 1
[INPUT]
Review reports contain 2 gold-level practices and 1 platinum practice. Dev notes contain several errors and solutions.

[BAD-DECISION]
Include both gold and platinum practices in best-practices.md to make the knowledge base look more comprehensive. Self-judge that some gold practices are actually platinum quality and promote them without review evidence.

[WHY-BAD]
Violates Constraint 1 (only platinum practices) and Constraint 2 (no self-judgment on practice levels). Including non-platinum practices dilutes knowledge base quality. Self-promotion of practices contradicts trust-review-markings principle. Creates unreliable knowledge base.

[CORRECT-APPROACH]
Extract only the 1 platinum practice marked in review reports. Document gold practices separately as "promising practices pending validation" or exclude them entirely. Trust review markings without self-judgment. Create best-practices.md with only validated platinum-level entries. Annotate: "2 gold-level practices excluded pending platinum validation."

### Bad Example 2
[INPUT]
Review reports show conflicting practices: one recommends synchronous API calls for reliability, another recommends async for performance. Both marked platinum.

[BAD-DECISION]
Choose the async approach because it seems more modern and better. Document only async approach in best-practices-api-design.md. Discard synchronous approach to avoid confusion.

[WHY-BAD]
Violates Constraint 3 (do not force resolution of conflicts). Choosing one approach loses valuable context. Both practices may be valid in different scenarios. Removing evidence prevents context-based decisions.

[CORRECT-APPROACH]
Preserve both approaches in best-practices-api-design.md. Document Approach A (synchronous) with evidence source and applicable scenarios (critical data consistency). Document Approach B (async) with evidence source and applicable scenarios (high-throughput systems). Annotate conflict point: Both approaches are platinum-validated for different contexts. Let developers choose based on their specific requirements.

## [Example]
  **Knowledge Management Architecture**:
  
  1. **Document Types & Naming Convention**:
     - Best Practices: `best-practices-{semantic-topic}.md` (記錄 platinum 級別的開發實踐)
     - Errors: `errors-{semantic-topic}.md` (記錄已知錯誤和快速解決方案)
     - Problem Solving: `problem-solving-{semantic-topic}.md` (記錄複雜問題的完整解決過程)
  
  2. **Semantic Classification Examples**:
     - Best Practices topics: api-design, error-handling, testing-strategy, code-organization, dependency-management
     - Errors topics: authentication, database, api-integration, deployment, configuration
     - Problem Solving topics: performance, scalability, security, data-migration, integration
  
  3. **Document Format Templates**:
  
  **best-practices-{topic}.md**:
  ```markdown
  # {Topic} Best Practices
  
  ## {Practice Title}
  
  **Description**: {簡述最佳實踐}
  
  **Evidence Source**: {evidence_path}
  
  **Applicable Scenarios**: {適用場景}
  
  **Level**: Platinum
  ```
  
  **errors-{topic}.md**:
  ```markdown
  # {Topic} Errors
  
  ## {Error Title}
  
  **Error Type**: {錯誤類型}
  
  **Context**: {發生情境}
  
  **Solution**: {解決方案}
  
  **Source**: {evidence_path}
  ```
  
  **problem-solving-{topic}.md**:
  ```markdown
  # {Topic} Problem Solving
  
  ## {Problem Title} ({YYYY-MM-DD})
  
  **Problem**: {問題描述}
  
  **Investigation**: {調查過程}
  
  **Root Cause**: {根本原因分析}
  
  **Solution**: {解決方案}
  
  **Decision Rationale**: {決策理由}
  
  **Prevention**: {預防措施}
  
  **Source**: {evidence_path}
  ```
  
  4. **Concrete Examples**:
  
  **Example 1: best-practices-{topic}.md**
  ```markdown
  # {Topic} Best Practices
  
  ## {Practice Title A}
  
  **Description**: {具體描述該最佳實踐的內容和價值}
  
  **Evidence Source**: {evidence_path}
  
  **Applicable Scenarios**: {描述該實踐適用的場景和條件}
  
  **Level**: Platinum
  
  ## {Practice Title B}
  
  **Description**: {具體描述該最佳實踐的內容和價值}
  
  **Evidence Source**: {evidence_path}
  
  **Applicable Scenarios**: {描述該實踐適用的場景和條件}
  
  **Level**: Platinum
  ```
  
  **Example 2: errors-{topic}.md**
  ```markdown
  # {Topic} Errors
  
  ## {Error Title A}
  
  **Error Type**: {錯誤分類，如 Security Vulnerability / Logic Error / Configuration Error}
  
  **Context**: {描述錯誤發生的情境和觸發條件}
  
  **Solution**: {描述解決方案的具體步驟或方法}
  
  **Source**: {evidence_path}
  
  ## {Error Title B}
  
  **Error Type**: {錯誤分類}
  
  **Context**: {描述錯誤發生的情境和觸發條件}
  
  **Solution**: {描述解決方案的具體步驟或方法}
  
  **Source**: {evidence_path}
  ```
  
  **Example 3: problem-solving-{topic}.md**
  ```markdown
  # {Topic} Problem Solving
  
  ## {Problem Title} ({YYYY-MM-DD})
  
  **Problem**: {清楚描述遇到的問題現象和影響範圍}
  
  **Investigation**: 
  - {調查步驟1：使用的工具或方法，以及發現的線索}
  - {調查步驟2：進一步的分析過程和結果}
  - {調查步驟3：額外的數據收集或驗證}
  
  **Root Cause**: 
  1. {根本原因1：技術層面的具體原因}
  2. {根本原因2：設計或配置層面的原因}
  
  **Solution**: 
  1. {解決方案1：具體的修復措施}
  2. {解決方案2：相關的配置或代碼調整}
  3. {解決方案3：補充的優化措施}
  
  **Decision Rationale**: 
  - {決策理由1：為什麼選擇這個方案而非其他方案}
  - {決策理由2：該方案的優勢和權衡考量}
  - {決策理由3：預期效果和可接受的代價}
  
  **Prevention**: 
  - {預防措施1：流程或工具層面的改進}
  - {預防措施2：技術實踐的建議}
  - {預防措施3：代碼審查或測試的重點}
  
  **Source**: {evidence_path}
  ```
  
  5. **Classification Guidelines**:
     - 根據內容的語義和主題進行分類，而非技術層或模組
     - 同一 semantic topic 可能跨越多個技術層（如 authentication 可能涉及 frontend, backend, database）
     - 優先選擇對 LLM 和人類都友好的語義分類詞彙
     - 當單個文件內容過多（超過 50 個條目）時，考慮進一步細分語義主題
