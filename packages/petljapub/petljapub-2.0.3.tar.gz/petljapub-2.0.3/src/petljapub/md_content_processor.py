import os
from . import markdown_magic_comments
from . import md_util
from . import yaml_specification
from . import logger

# Base class for all output organizers

# Output organizers map the logical hierarchy given by the yaml file
# (and physical hierarchy of the input files) to the physical
# hierarchy of output files
class OutputOrganizer:
    def __init__(self):
        pass

    def output_dir(section_path):
        pass

# All output files are put into a single directory
class OutputOrganizerSingleDir(OutputOrganizer):
    def __init__(self, output_dir):
        self._output_dir = output_dir

    def output_dir(self, section_path):
        return self._output_dir
    

# Output hiearchy matches the one given by the YAML file
class OutputOrganizerHierarchy(OutputOrganizer):
    def __init__(self, base_dir="."):
        self._base_dir = base_dir
    
    def output_dir(self, section_path):
        return os.path.join(self._base_dir, section_path)

class ImageProcessor:
    def process(self, section_path, md_file_path, md):
        # process all images
        for (title, image) in md_util.images_in_md(md):
            logger.info("Copy image:", image)
            input_dir = os.path.dirname(md_file_path)
            src_image_path = os.path.join(input_dir, image)
            self.process_image(src_image_path, section_path, os.path.dirname(image))
        return md

    def process_image(self, src_image_path, section_path, relative_dir):
        pass

class ImageProcessorCopy(ImageProcessor):
    def __init__(self, writer, output_organizer):
        self._writer = writer
        self._output_organizer = output_organizer

    def process_image(self, src_image_path, section_path, relative_dir):
        image = os.path.basename(src_image_path)
        dst_dir = self._output_organizer.output_dir(section_path)
        dst_image_path = os.path.join(dst_dir, relative_dir, image)
        self._writer.copy_file(src_image_path, dst_image_path)

class LinkProcessor:
    def process(self, current_dir, current_file, md):
        pass
        
class LinkProcessorRaw(LinkProcessor):
    def process(self, current_dir, current_file, md):
        for (link_title, link_id) in md_util.links_in_md(md):
            md = md_util.replace_link(md, link_title, link_id, "[{}]".format(md_util.italic(link_id)))
        return md

class LinkProcessorPublication(LinkProcessor):
    def __init__(self, yaml_specification, task_repo):
        self._yaml_specification = yaml_specification
        self._task_repo = task_repo

    def exclude_links_not_in_publication(self, md):
        def do_exclude(lines):
            links_in_pub = True
            for (_, link_id) in md_util.links_in_md("".join(lines)):
                if  not self._yaml_specification.contains_task(link_id):
                    links_in_pub = False
                    break
            return lines if links_in_pub else []

        md = markdown_magic_comments.process_by_key_value(md, "span", "link",
                                                          do_exclude)
        return md
    

    def process(self, section_path, md_file_path, md):
        md = self.exclude_links_not_in_publication(md)
        for (link_title, link_id) in md_util.links_in_md(md):
            if link_title or ("/" in link_id):
                # links should only contain task or section ids
                # raw links are kept unchanged
                logger.warn("raw link", link_title, link_id, " is left unchanged")
            elif self._task_repo.contains_task(link_id):
                # find the title of the linked task
                task_title = self._task_repo.task(link_id).title()
                # find the sections that it occurrs in
                task_sections = self._yaml_specification.sections_containing_task(link_id)
                if task_sections:
                    # assume that links points to the first task occurrence
                    task_section = task_sections[0]
                    md = self.format_link(md, link_title, link_id, task_section, task_title, section_path)
                else:
                    # warn if the task exists, does not occurr in the publication, and remove link
                    # (only print the linked task title in italic)
                    md = md_util.replace_link(md, link_title, link_id, md_util.italic(task_title))
                    logger.warn(section_path, md_file_path, "- link to task", link_id, "not in publication")
            # elif self._publication_repo.contains(link_id): TODO
            else:
                logger.error("non-existent link", link_id, "in", md_file_path)
        return md

    def format_link(self, md, link_title, link_id, task_section, task_title, section_path):
        pass

    
class LinkProcessorNoLinks(LinkProcessorPublication):
    def __init__(self, yaml_specification, task_repo):
        super().__init__(yaml_specification, task_repo)

    def format_link(self, md, link_title, link_id, task_section, task_title, current_dir):
        return md_util.replace_link(md, link_title, link_id, md_util.italic(task_title))
    
class LinkProcessorTex(LinkProcessorPublication):
    def __init__(self, yaml_specification, task_repo):
        super().__init__(yaml_specification, task_repo)

    def format_link(self, md, link_title, link_id, task_section, task_title, current_dir):
        return md_util.change_link(md, link_title, link_id, task_title, "#" + link_id) 

class LinkProcessorHTML(LinkProcessorPublication):
    def __init__(self, yaml_specification, task_repo, output_organizer):
        super().__init__(yaml_specification, task_repo)
        self._output_organizer = output_organizer

    def task_output_dir(self, task_id, task_section):
        task = self._task_repo.task(task_id)
        return self._output_organizer.output_dir(os.path.join(task_section, task.id()))
    
    def format_link(self, md, link_title, link_id, task_section, task_title, current_dir):
        link_target = os.path.join(self.task_output_dir(link_id, task_section), link_id + "-st.html")
        link_path = os.path.relpath(link_target, current_dir)
        return md_util.change_link(md, link_title, link_id, task_title, link_path)
    
class MDContentProcessor:
    def __init__(self, link_processor, image_processor):
        self._link_processor = link_processor
        self._image_processor = image_processor
        pass

    def process(self, section_path, md_file_path, md, langs=None, level=None, unnumbered=False, unlisted=False):
        # the name of the file
        md_file_name = os.path.basename(md_file_path)
        
        # exclude divs marks for exclusion
        md = markdown_magic_comments.exclude(md, "div", ["exclude"])
        # format remaining divs
        md = markdown_magic_comments.format_divs(md)

        # degrade headings
        if level != None:
            md = md_util.degrade_headings(md, level, unnumbered=unnumbered, unlisted=unlisted)

        # process links
        if self._link_processor != None:
            md = self._link_processor.process(section_path, md_file_path, md)
        
        # process images
        if self._image_processor != None:
            md = self._image_processor.process(section_path, md_file_path, md)


        # process languages
        if langs == None:
            return md
        else:
            lang_md = {}
            for lang in langs:
                lang_md[lang] = markdown_magic_comments.exclude_all_except(md, "lang", langs)
            return lang_md
